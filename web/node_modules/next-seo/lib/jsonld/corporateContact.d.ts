import React from 'react';
import { JsonLdProps } from './jsonld';
import type { ContactPoint } from 'src/types';
export interface CorporateContactJsonLdProps extends JsonLdProps {
    url: string;
    contactPoint: ContactPoint[];
    logo?: string;
}
declare function CorporateContactJsonLd({ type, keyOverride, contactPoint, ...rest }: CorporateContactJsonLdProps): React.JSX.Element;
export default CorporateContactJsonLd;
