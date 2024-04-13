import React from 'react';
import { JsonLdProps } from './jsonld';
export interface SocialProfileJsonLdProps extends JsonLdProps {
    type: 'Person' | 'Organization';
    name: string;
    url: string;
    sameAs: string[];
}
declare function SocialProfileJsonLd({ type, keyOverride, ...rest }: SocialProfileJsonLdProps): React.JSX.Element;
export default SocialProfileJsonLd;
